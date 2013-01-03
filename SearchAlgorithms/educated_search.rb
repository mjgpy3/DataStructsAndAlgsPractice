# Requires a sorted array, makes an educated guess
# on the index of the desired value and goes from
# there. Works very well with an evenly distributed
# array.
def educated_search(array, val)
  # Make sure the value is in the bounds of the array
  return nil if not (val >= array[0] and val <= array[-1])  

  # Generate a guess index
  i = ((val.to_f - array[0])/(array[-1]-array[0])*array.count).to_i

  # If the index is larger than possible, reduce it,
  # then see if we found it.
  i = array.count-1 if i > array.count-1
  return i if array[i] == val

  # If we're below the desired value, loop up
  # Otherwise loop down
  if array[i] < val
    while array[i] < val and i < array.count-1
      i += 1
      return i if array[i] == val
    end
  else
    while array[i] > val and i > 0
      i -= 1
      return i if array[i] == val
    end
  end

  # If not found, return nil
  return nil
end

a = [-20, -15, -10, -9, -8, -6, -5, -4, -3, 0, 1,2,3,5,7,8,12,14,15,17,20]

a.each do |x|
  puts educated_search(a, x)
end
