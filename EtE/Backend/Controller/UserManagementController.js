var mongoose = require("mongoose");
Message = mongoose.model("User");

exports.createUser = function(req, res) {
    var salt = crypto.randomBytes(32).toString('base64');
    var scryptParams = scrypt.paramsSync(0.5)
    var user = new User({
            name: req.body.name,
            password: scrypt.hash(req.body.password, scryptParams, 256, user.salt),
            salt: salt
    });
    nick.save(function(err) {
        if (err) throw err;

        console.log('User saved successfully');
        res.json({ success: true });
    });
}