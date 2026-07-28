class Solution {
    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> result = new ArrayList<>();
        //sort intervals by start interval
        for(int i = 0; i < intervals.length; i++){
            int index = 0;
            while (index < result.size() && result.get(index)[0] < intervals[i][0]) {
                index++;
            }
            result.add(index, intervals[i]);
        }

        
        int i = 1;
        while (i < result.size()) {
            int[] prev = result.get(i - 1);
            int[] cur  = result.get(i);
            if (cur[0] <= prev[1]) {
                // extend prev's end to cover cur, then drop cur
                prev[1] = Math.max(prev[1], cur[1]);
                result.remove(i);   // note: do NOT i++ here
            } else {
                i++;
            }
        }

    return result.toArray(new int[result.size()][]);
    }
}
