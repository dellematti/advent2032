public class Card {

    private final Rank rank;

    public Card (Rank rank) {
        this.rank = rank;
    }

    public Rank getRank() {
        return rank;
    }

    @Override
    public String toString() {
        return rank.toString();
    }


}