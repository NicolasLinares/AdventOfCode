import re

def test1_CheckPolymer(filename, STEPS, expected):
    input = open(filename, 'r').readlines()
    (polymer, rules) = ParseInput(input)
    result = FindOptimalPolymer(polymer, rules, STEPS)
    assert(result == expected)

def test2_CheckQuantity(filename, STEPS, expected):
    input = open(filename, 'r').readlines()
    (polymer, rules) = ParseInput(input)
    polymer = FindOptimalPolymer(polymer, rules, STEPS)
    result = GetQuantity(polymer)
    assert(result == expected)

def ParseRule(rule):
    return rule.split(' -> ')

def MatchRule(pair, rules):
    for rule in rules:
        rule = ParseRule(rule)
        if pair == rule[0]:
            return rule[1]
    return None

def FindOptimalPolymer(polymer, rules, STEPS):
    for step in range(STEPS):
        i = 0
        match = None
        while i < len(polymer) + 1:
            limit = i + 2
            pair = polymer[i:limit]
            match = MatchRule(pair, rules)
            if match:
                polymer = polymer[:limit-1] + match + polymer[limit-1:]
                i += 2
            else:
                i += 1
    return polymer

def GetQuantity(polymer):
    dic = dict()
    for element in polymer:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1
    mostCommon = dic.get(max(dic, key=dic.get))
    leastCommon = dic.get(min(dic, key=dic.get))
    return mostCommon - leastCommon

def ParseInput(input):
    polymer = input[0].strip()
    rules = []
    for line in input:            
        if re.match("[A-Z]{2} -> [A-Z]", line):
            rule = line.strip()
            rules.append(rule)

    return (polymer, rules)

def main(filename):
    input = open(filename, 'r').readlines()
    (polymer, rules) = ParseInput(input)
    STEPS = 10
    polymer = FindOptimalPolymer(polymer, rules, STEPS)
    total = GetQuantity(polymer)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckPolymer('test.in', 1, 'NCNBCHB')
test1_CheckPolymer('test.in', 2, 'NBCCNBBBCBHCB')
test1_CheckPolymer('test.in', 3, 'NBBBCNCCNBBNBNBBCHBHHBCHB')
test1_CheckPolymer('test.in', 4, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

test2_CheckQuantity('test.in', 1, 1)
test2_CheckQuantity('test.in', 2, 5)
test2_CheckQuantity('test.in', 3, 7)
test2_CheckQuantity('test.in', 4, 18)

# program
main("input.in")