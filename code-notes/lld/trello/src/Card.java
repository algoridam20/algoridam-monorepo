import java.util.Optional;

public class Card {
    private String id;
    private String name;
    private String description;
    private User assignedUser;

    public Card(String id, String name, String description) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.assignedUser = null;
    }

    public Card(String id, String name, String description, User assignedUser) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.assignedUser = assignedUser;
    }
}
