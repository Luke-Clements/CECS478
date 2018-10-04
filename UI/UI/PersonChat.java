/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UI;

import javafx.scene.control.Label;

/**
 *
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
