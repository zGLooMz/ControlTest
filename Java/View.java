import java.util.Scanner;

public class View {

    private ToysList tl = new ToysList<>();

    public void run() {

        Commands com = Commands.NONE;

        while (true) {
            String command = prompt("Type the command (LOAD, LIST, PLAY, EXIT): ");
            try {
                com = Commands.valueOf(command);
            } catch (IllegalArgumentException e) {
                System.out.println("Command doesn't exist");
            }
            if (com == Commands.EXIT)
                return;
            try {
                switch (com) {
                    case LOAD:
                        Toy toy = setToy();
                        tl.loadToy(toy);
                        break;
                    case LIST:
                        System.out.println(tl);
                        break;
                    case PLAY:
                        tl.getToy();
                        break;
                }
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }

    }

    private Toy setToy() {
        String id = prompt("Id: ");
        String name = prompt("Name: ");
        String weigth = prompt("Weight: ");
        String amount = prompt("Amount: ");
        return new Toy(id, name, weigth, amount);
    }

    private String prompt(String message) {
        Scanner in = new Scanner(System.in);
        System.out.print(message);
        return in.nextLine();
    }

}