class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let p = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        let open = Object.values(p);
        let stack = [];
        for (let i = 0; i < s.length; i++) {
            if (open.includes(s[i]))
                stack.push(s[i]);
            else if (stack.pop() !== p[s[i]])
                return false;
        }
        return stack.length === 0;
    }
}
