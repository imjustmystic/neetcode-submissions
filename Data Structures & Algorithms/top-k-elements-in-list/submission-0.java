class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> nMap = new HashMap<>();
        
        for(int i : nums){
            if(nMap.containsKey(i)){
                nMap.put(i,nMap.get(i)+1);
            }else{
                nMap.put(i,1);
            }
            
        }

        List<Integer> values = new ArrayList<Integer>(nMap.values());
        values.sort(null);
        List<Integer> freqNums = new ArrayList<Integer>();
        for(int i = values.size()-1; i >= values.size() - k; i--){
            for (Map.Entry<Integer, Integer> entry : nMap.entrySet()) {
                if (entry.getValue().equals(values.get(i)) && !freqNums.contains(entry.getKey())) {
                    freqNums.add(entry.getKey());
                    break;
                }
            }
        }
        
        int[] result = new int[freqNums.size()];
        for (int j = 0; j < freqNums.size(); j++) {
            result[j] = freqNums.get(j);
        }
        return result;

    }
}