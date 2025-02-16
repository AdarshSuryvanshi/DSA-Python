""" 
Q..
Python implementation of the Search Query Autocomplete System using a Trie with HashMap to efficiently store and retrieve sentence suggestions.
"""

""" 
🚀 Concept: Trie (Prefix Tree) + HashMap
 1) Trie Structure:
Each node stores a dictionary of child nodes for fast prefix searching.
Each node maintains a HashMap of sentence frequencies.

2) Efficient Searching:
On each character input, traverse the Trie to find matching sentences.
Sort results by frequency and ASCII order to return the top

3) Sentence Storage:
When a user types #, store the new sentence in the Trie.

"""
""" 
Q..
Python implementation of the Search Query Autocomplete System using a Trie with HashMap to efficiently store and retrieve sentence suggestions.
"""

from collections import defaultdict

class TrieNode:
    """ Trie Node to store sentences and their frequencies """
    def __init__(self):
        self.children = {}  # Dictionary to store next characters
        self.freq_map = defaultdict(int)  # HashMap to store sentence frequencies

class AutoCompleteSystem:
    """ AutoComplete System using Trie + HashMap """
    def __init__(self, sentences, times):
        """
        Initializes the system with previously searched sentences.
        :param sentences: List of past sentences.
        :param times: Corresponding frequencies of past sentences.
        """
        self.root = TrieNode()  # Root of the Trie
        self.current_input = ""  # Stores the ongoing user input
        self.current_node = self.root  # Pointer to traverse Trie
        
        # Insert all previous sentences into the Trie
        for sentence, freq in zip(sentences, times):
            self._insert(sentence, freq)

    def _insert(self, sentence, freq):
        """
        Inserts a sentence with given frequency into the Trie.
        :param sentence: The sentence to be stored.
        :param freq: Frequency count of the sentence.
        """
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.freq_map[sentence] += freq  # Update frequency in each node

    def _search_top_3(self):
        """
        Searches for the top 3 most frequent sentences with current prefix.
        :return: List of top 3 matching sentences.
        """
        if not self.current_node:
            return []

        # Sort sentences first by frequency (descending) then lexicographically (ascending)
        sorted_sentences = sorted(self.current_node.freq_map.keys(), 
                                  key=lambda s: (-self.current_node.freq_map[s], s))
        return sorted_sentences[:3]

    def input(self, c):
        """
        Processes the next character input by the user.
        :param c: The next character typed.
        :return: List of top 3 autocomplete suggestions.
        """
        if c == "#":
            # Store the completed sentence in the Trie
            self._insert(self.current_input, 1)
            self.current_input = ""  # Reset input for new search
            self.current_node = self.root  # Reset pointer
            return []

        self.current_input += c  # Add character to input
        if self.current_node and c in self.current_node.children:
            self.current_node = self.current_node.children[c]
        else:
            self.current_node = None  # No matching sentences
        
        return self._search_top_3()
""" 

🔥 How the Code Works
Initialization:

The AutoCompleteSystem is initialized with past search data.
The _insert() function builds a Trie storing sentence frequencies.
Handling User Input (input(char c)):

If the input is #, the sentence is saved.
Otherwise, the system searches for sentences matching the prefix.
It returns the top 3 most frequent sentences in the correct order

🏆 Time Complexity Analysis
Insertion (_insert()): 
O(L), where 
L is the sentence length.
Searching (_search_top_3()):
Traversing the Trie: 
O(L).
Sorting: 
O(NlogN) (for small N ≤ 102, sorting is negligible).

"""

### Example of Excution 
# Initialize autocomplete system
auto = AutoCompleteSystem(["i love you", "island", "ironman", "i love geeksforgeeks"], [5,3,2,2])

# User starts typing "i"
print(auto.input('i'))  # Output: ["i love you", "island", "i love geeksforgeeks"]

# User types space "i "
print(auto.input(' '))  # Output: ["i love you", "i love geeksforgeeks"]

# User types "a"
print(auto.input('a'))  # Output: []

# User completes input with '#'
print(auto.input('#'))  # Output: []

""" 
Why This Approach?
✅ Optimized: Trie ensures quick prefix searching.
✅ Sorted Output: Sorting by frequency and ASCII ensures correct results.
✅ Handles New Inputs: Dynamically adds new sentences to the system.
"""