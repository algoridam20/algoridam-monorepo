public class Split {
    private String userName;
    private int amount;

    public Split(String userName, int amount) {
        this.userName = userName;
        this.amount = amount;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String stringName) {
        this.userName = userName;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    @Override
    public String toString() {
        return "Gets "+ amount +"$ From "+ userName +" ";
    }
}
