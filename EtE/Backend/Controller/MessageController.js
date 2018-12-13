var mongoose = require("mongoose");
Message = mongoose.model("Message");

exports.createMessage = function(req, res) {
    var newMessage = new Message();
    newMessage.from = req.body.from;
    newMessage.to = req.body.to;
    newMessage.data = req.body.data;
    newMessage.save(function(err) {
      if (err)
        res.send(err);
      res.json({status: "success", newMessage});
    });
};

exports.getMessage = function(req, res) {
    Message.find({toId: req.params.toId})
    Message.findById(req.params.message_id, function(err, message) {
      if (err)
        res.send(err);
      res.json(message);
    });
}

exports.deleteMessage = function(req, res) {
    Message.remove({
      _id: req.params.message_id
    }, function(err, message) {
      if (err)
        res.send();
      res.json({status: "success", message: 'Message deleted'});
    });
}