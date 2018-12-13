var mongoose = require("mongoose");
Message = mongoose.model("Message");

exports.authenticate = function(req, res){
    console.log(req.body.name);
    // find the user
    User.findOne({
        name: req.body.name
    }, function(err, user) {
  
        if (err) throw err;
    
        if (!user) {
            res.json({ success: false, message: 'Authentication failed. User not found.' });
        } else if (user) {
            var scryptParams = scrypt.paramsSync(0.5);
            var passwordHash = scrypt.hash(req.body.password, scryptParams, 256, user.salt);
            // check if password matches
            if (passwordHash != user.passwordHash) {
            res.json({ success: false, message: 'Authentication failed. Wrong password.' });
            } else {
    
            // if user is found and password is right
            // create a token with only our given payload
            // we don't want to pass in the entire user since that has the password
            const payload = {
                admin: user.admin     };
                var token = jwt.sign(payload, httpApp.get('superSecret'));
        
                // return the information including token as JSON
                res.json({
                    success: true,
                    message: 'Enjoy your token!',
                });
            }
        }
  });
};

exports.getMessage = function(req, res) {
    Message.findById(req.params.message_id, function(err, message) {
        if (err)
            res.send(err);
        res.json(message);
    });
}