class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = {}
        answer = []
        for i, element in enumerate(strs):
            new_map = {}
            for char in element:
                if char in new_map:
                    new_map[char] += 1
                else:
                    new_map[char] = 1
            if tuple(sorted(new_map.items())) in outputs.keys():
                outputs[tuple(sorted(new_map.items()))].append(element)
            else:
                outputs[tuple(sorted(new_map.items()))] = [element]
            #print(sorted(tuple(new_map.items())))
        return list(outputs.values())