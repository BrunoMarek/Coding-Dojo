public class ProjectTest {
    public static void main(String[] args){
        Project x = new Project();
        Project y = new Project("Marek");
        Project z= new Project("Marek", "Buy bitcoin");

        // System.out.println(z.getName());
        // System.out.println(z.getDescription());
        // x.setName("ADA");
        // x.setDescription("Best Crypto");
        // System.out.println(x.getName());
        // System.out.println(x.getDescription());
        // z.setName("SLP");
        // z.setDescription("BREED AXIE");
        // System.out.println(z.getName());
        // System.out.println(z.getDescription());
        System.out.println(z.elevatorPitch());
    }
}
