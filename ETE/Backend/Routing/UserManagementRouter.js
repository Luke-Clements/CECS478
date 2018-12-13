module.exports = function(app) {
    var userManagementController = require("../Controllers/UserManagementController");

    //Save user
    app.route('/signup')
        .post(userManagementController.createUser);
    // //Save user
    // router.post('/signup', function(req, res) {
    // var nick = new User({
    //         name: req.body.name,
    //         password: req.body.password,
    //         admin: false
    // });
    // nick.save(function(err) {
    //     if (err) throw err;

    //     console.log('User saved successfully');
    //     res.json({ success: true });
    // });
    // });
}