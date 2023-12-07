import java.util.HashMap;

public class FourOfAKindEvaluator implements ChainedHandEvaluator{
    public ChainedHandEvaluator next;
    public FourOfAKindEvaluator(ChainedHandEvaluator nextEvaluator){
        next = nextEvaluator;
    }
    @Override
    public HandRank handEvaluator(PokerHand hand) {
        HashMap<Rank, Integer> map = new HashMap<>();
        for(Card card : hand){
            Rank rank = card.getRank();
            if(map.containsKey(rank)) {
                map.put(rank, map.get(rank)+1);
            }else{
                map.put(rank, 1);
            }
        }
        if (map.containsValue(4)) return HandRank.FOUR_OF_A_KIND;
        return next.handEvaluator(hand);
    }
}
