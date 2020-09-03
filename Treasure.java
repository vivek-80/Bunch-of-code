package treasurehunt;

public class Treasure {

public int POSITIONS_PER_ROW = 20;
public int MAX_DISTANCE = 401;
private String name;
private int xLocation;
private int yLocation;
private Boolean found;


    public Treasure(){
     name = "";
     xLocation = 0;
     yLocation = 0;
     found = false;
    }

    public Treasure(String name){
        this.name = name;
        xLocation = 0;
        yLocation = 0;
        found = false;
    }

    public int getXLocation(){
        return xLocation;
    }

    public int getYLocation(){
        return yLocation;
    }

    public boolean isFound(){
        return found; 
    }

    public void hideTreasure(){
        xLocation = 1+(int)(Math.random()*POSITIONS_PER_ROW);
        yLocation = 1+(int)(Math.random()*POSITIONS_PER_ROW);
    }

    public int treasureStatus(int xStick , int yStick){
     if (xStick == xLocation && yStick == yLocation){
        return 0;
    } else if (xStick != xLocation || yStick != yLocation) {
        return Math.abs((yStick-yLocation)+(xStick-xLocation));           
    } else return MAX_DISTANCE;



}


}