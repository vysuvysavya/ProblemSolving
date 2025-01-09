class Solution {
    public ArrayList<ArrayList<String>> anagrams(String[] arr) {
        Map<String, ArrayList<String>> map = new HashMap<>();

        // Step 1: Group words based on their sorted version
        for (String str : arr) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);

            // Check if the sorted string exists as a key in the map
            if (!map.containsKey(sortedStr)) {
                map.put(sortedStr, new ArrayList<>());
            }
            // Add the original word to the corresponding group
            map.get(sortedStr).add(str);
        }

        // Step 2: Collect all groups from the map into the result list
        ArrayList<ArrayList<String>> result = new ArrayList<>(map.values());

        // Step 4: Sort the groups based on the first string in each group
        result.sort((a, b) -> a.get(0).compareTo(b.get(0)));

        return result;
    }
}

=======================================================================================


Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.


Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.
