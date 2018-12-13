var express = require('express');
var httpApp = express();
var http = require('http');
var router = express.Router();
var Message = require('./models/message');
var mongoose = require('mongoose');
var crypto = require("crypto");

function GenerateSalt() {
    return crypto.randomBytes(32).toString('base64');
}
function HashPasswordSHA256(password, salt) {
    var hash = crypto.createHash('SHA256', salt);
    hash.update(password);
    return hash.digest('base64');
}

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost');

// JWT
var jwt = require('jsonwebtoken'); //Create, sign, verify tokens
var config = require('./config'); //Get Config
var User = require('./models/user'); //Get Mongoose model
var bodyParser = require('body-parser');
var morgan = require('morgan');

//Config
httpApp.set('superSecret', config.secret); // secret variable

// use body parser so we can get info from POST and/or URL parameters
httpApp.use(bodyParser.urlencoded({ extended: false }));
httpApp.use(bodyParser.json());

// use morgan to log requests to the console
httpApp.use(morgan('dev'));
httpApp.use(express.static("./public"));

//Save user
router.post('/signup', function(req, res) {
    console.log(req.body)
    console.log(req.body.name)
    var salt = GenerateSalt();
    var user = new User({
            username: req.body.name,
            password: HashPasswordSHA256(req.body.password, salt),
            admin: false,
            salt: salt
    });
    user.save(function(err) {
            if (err) throw err;

            console.log('User saved successfully');
            res.json({ success: true, userId: user.id });
    });
});

//Authenticate a user
router.post('/authenticate', function(req, res){
    console.log(req.body);
    console.log(req.header);
    console.log(req.body.name);
    // find the user
    User.findOne({username: req.body.name}, function(err, user) {
            if (err) throw err;
            if (!user) {
                    res.json({ success: false, message: 'Authentication failed.' });
            } else if (user) {
                    var passwordHash = HashPasswordSHA256(req.body.password, user.salt);
                    console.log(passwordHash);
                    console.log(user.password);
                    // check if password matches
                    if (passwordHash != user.password) {
                        res.status(403).send({
                                success: false,
                                message: 'Invalid Credentials'
                        })
                    } else {
                            // if user is found and password is right
                            // create a token with only our given payload
                            // we don't want to pass in the entire user since that has the password

                            const payload = {admin: user.admin};
                                var token = jwt.sign(payload, httpApp.get('superSecret'));

                                // return the information including token as JSON
                                res.json({token: token});
                        }
                }
        });
});

//middleware
router.use(function(req, res, next) {
        // check header or url parameters or post parameters for token
        var token = req.body.token || req.query.token || req.headers['x-access-token'];

        // decode token
        if (token) {

                // verifies secret and checks exp
                jwt.verify(token, httpApp.get('superSecret'), function(err, decoded) {
                        if (err) {
                                return res.json({ success: false, message: 'Failed to authenticate token.' });
                        } else {
                                // if everything is good, save to request for use in other routes
                                req.decoded = decoded;
                                next();
                        }
                });
        } else {
                // if there is no token
                // return an error
                return res.status(403).send({
                        success: false,
                        message: 'No token provided.'
                });
         }
});

//remaining routes
router.route('/Message')
.post(function(req, res) {
    var newMessage = new Message();
    newMessage.toId = req.body.toId;
    newMessage.fromId = req.body.fromId;
    newMessage.data = req.body.data;
    newMessage.save(function(err) {
            if (err)
                    res.send(err);
        res.json({status: "success", newMessage});
            });
    });
router.route('/Message/:toId')
.get(function(req, res) {
    console.log(req.params)
    console.log(req.params.toId)
    Message.find({"toId": req.params.toId}, function(err, message) {
            if (err)
                    res.send(err);
        res.json({message});
            });
    });
router.route('/DeleteMessages/:toId')
.delete(function(req, res) {
    Message.deleteMany({"toId": req.params.toId}, function(err, message) {
            if (err)
                    res.send();
        res.json({message});
            });
    });

httpApp.use('/app', router);
http.createServer(httpApp).listen(3000, () => {console.log("Server Connected")});