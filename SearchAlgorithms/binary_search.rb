def binary_search(array, val, beg=0, last=nil)
  last = array.count if last == nil

  half = (beg+last)/2

  return half if array[half] == val
  return nil if half == beg or half == last
  return binary_search(array, val, half, last) if array[half] < val
  return binary_search(array, val, beg, half)  if array[half] > val
end

search_me = ["Michael", "something", "foobar", "github", "Django"]

search_me = search_me.sort

p search_me

puts "Michael found at #{binary_search(search_me, 'Michael')}"
puts "Foobar found at #{binary_search(search_me, 'Foobar')}"

