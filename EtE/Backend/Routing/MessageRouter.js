module.exports = function(app) {
    var messageController = require("../Controllers/MessageController");

//Message routes
app.route('/Message')
    .post(messageController.createMessage);
app.route('/Message/:message_id')
    .get(messageController.getMessage);
app.route('/deleteMessage/:message_id')
    .delete(messageController.deleteMessage);
}