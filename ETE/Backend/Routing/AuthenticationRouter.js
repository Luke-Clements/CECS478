module.exports = function(app) {
    var authenticationController = require("../Controllers/AuthenticationController");

//Authenticate a user
app.route('/authenticate')
    .post(authenticationController.authenticate);
}