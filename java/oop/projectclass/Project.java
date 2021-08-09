public class Project{
    // member variables here
    private String name;
    private String description;


    // constructor methods
    public Project(){
        this.name = "Project";
        this.description = "proj desc";
    }

    public Project(String name){
        this.name = name;
        this.description = "proj desc";
    }

    public Project(String name, String description){
        this.name = name;
        this.description = description;
    }

    // methods
    public String elevatorPitch(){
        String pitch = String.format("%s %s", this.name, this.description);
        return pitch;
    }

    // getters
    public String getName(){
        return name;
    }
    public String getDescription(){
        return description;
    }

    // setters
    public void setName(String name){
        this.name = name;
    }
    public void setDescription(String description){
        this.description = description;
    }
}