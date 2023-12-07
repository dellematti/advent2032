public class HighCardEvaluator implements ChainedHandEvaluator{
    public HighCardEvaluator(){
    }
    @Override
    public HandRank handEvaluator(PokerHand hand) {
        return HandRank.HIGH_CARD;
    }
}
