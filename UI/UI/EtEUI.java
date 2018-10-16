package UI;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;

import javafx.application.Application;
import javafx.beans.binding.Bindings;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.SplitPane;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

/**
 *
 * @author lukecjm
 */
public class EtEUI extends Application {
    
    VBox window = new VBox();
    //For top of window
    HBox keyGenBox = new HBox();
    Button generateRSAKeyPair = new Button("Generate Key");
    Button viewRSAPublicKey = new Button("View Public Key");
    //for bottom of window
    SplitPane chatWindow = new SplitPane();
    //for left side of splitPane
    ScrollPane chats = new ScrollPane();
    ListView chatList;
    Label chatPerson;
    //for right side of splitPane
    VBox chatBox;
    TextField messageBox;
    Button send = new Button("Send");
    HBox messageSendBox;
    ScrollPane chat = new ScrollPane();
    VBox chatMessages;
    ObservableList<Node> chatNodes = FXCollections.observableArrayList();
    
    @Override
    public void start(Stage primaryStage) {
        //setup chats
        LoadChats();
        SetupChat();
        chatWindow.getItems().addAll(chats, chatBox);
        
        SetupKeyGen();
        window.getChildren().addAll(keyGenBox, chatWindow);
        
        Scene scene = new Scene(window, 700, 250);
        
        primaryStage.setTitle("EtE Chat");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    //Accomplishes the required actions involving the sending of a message to a
    //  known receiver
    public void Send() {
        boolean sent = true;
        PyObject encrypt = new PyObject();
        PythonInterpreter pi = new PythonInterpreter();
        pi.exec("from allEncryption import encrypt");
        encrypt = pi.get("encrypt");
        
        //run script to encrypt message
        PyObject ciphertext = encrypt.__call__(/*key*/ new PyString(messageBox.getText()));
        
        //send message to receiver
        if(sent){
            UpdateChat(messageBox.getText());
            UpdateChat(ciphertext.asString());
            //test decryption
        }
        //move selected PersonChat to the top of the chats pane
    }
    
    public void LoadChats() {
        chatList = new ListView();
        
        //test people in UI
        // replace with loading the save filelist of known RSA public key holders
        PersonChat pc = new PersonChat("Luke");
        PersonChat pc1 = new PersonChat("Marc");
        
        ObservableList<PersonChat> list = FXCollections.observableArrayList(pc, pc1);
        chatList.setItems(list);
        chats.setContent(chatList);
    }
    
    public void LoadChat(PersonChat person) {
        chatPerson.setText(person.toString());
        //update right SplitPane
        //  load the specific chat
    }
    
    public void UpdateChat(String message) {
        chatNodes.add(new MessageContainer(message, SpeechDirection.RIGHT));
//        System.out.println(message + ": " + chatNodes.size());
    }
    
    public void UpdatePeople(/*updated collection item*/) {
        //move updated collection item to the front of the collection
        //update UI
    }
    
    public void SetupKeyGen() {
        generateRSAKeyPair.setOnMouseClicked(e -> {
            GenerateKeyPair();
                });
        viewRSAPublicKey.setOnMouseClicked(e -> {
            //brings up window with copiable public key to show to new chat person
        });
        keyGenBox.getChildren().addAll(generateRSAKeyPair, viewRSAPublicKey);
    }
    
    private void GenerateKeyPair() {
        //run RSA key gen script in python
    }
    
    public void SetupChat() {
        chatPerson = new Label();
        messageBox = new TextField();
        messageSendBox = new HBox();
        chatBox = new VBox();
        chatMessages = new VBox();
        chat.setContent(chatMessages);
        messageSendBox.getChildren().addAll(messageBox, send);
        chatBox.getChildren().addAll(chatPerson, chat, messageSendBox);
        Bindings.bindContentBidirectional(chatNodes, chatMessages.getChildren());
        send.setDisable(true);
        messageBox.setOnKeyTyped(e -> {
            if(messageBox.getText().isEmpty()) {
                send.setDisable(true);
            }
            else {
                send.setDisable(false);
            }
        });
        send.setOnAction(e -> {
            Send();
            //UpdateChat(messageBox.getText());
        });
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
}
