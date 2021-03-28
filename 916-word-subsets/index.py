# @param {String[]} a
# @param {String[]} b
# @return {String[]}
# def word_subsets(a, b)
# 1
#     res = []
#     keywords = []
#     b.each do |x|
#         keywords.push(x.chars.map { |char| char*x.count(char)}.uniq.reject{|c| c.nil? || c.empty?})
#     end
#     keywords = keywords.flatten.uniq
#     a.each do |word|
#         res.push(word) if keywords.all?{|k| word.include?(k)}
#     end
#     res
# end

def word_subsets(a, b)
    res = []
    keywords = []
    b.each do |x|
        keywords.push(x.chars.map { |char| char*x.count(char)}.uniq.reject{|c| c.nil? || c.empty?})
    end
    keychars = keywords.flatten.uniq.map{|s| [s[0], s.size]}
    
    a.each do |word|
        mapping = keychars.select{|kc| word.count(kc[0]) >= kc[1]}
        res.push(word) if mapping.size == keychars.size
    end
    res
end
