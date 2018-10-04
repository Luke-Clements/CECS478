/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UI;

import javafx.scene.control.Label;

/**
 * This is a place holder for the column on the left listing the people's names
 * @author lukecjm
 */
public class PersonChat {
    private Label ps;
    
    public PersonChat(String name)
    {
        ps = new Label();
        ps.setText(name);
    }
    
    public Label getPersonChat()
    {
        return ps;
    }
    
    //will add an asterik to the beginning of a name if a message has not yet been read
    public void updatePersonChat(boolean viewed, String name)
    {
        if(!viewed){
            ps.setText("* " + name);
        }
        else {
            ps.setText(name);
        }
    }
}
