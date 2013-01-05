class Heap
  attr_accessor :root
  attr_reader :count

  def initialize
    @root = nil
    @count = 0
  end

  def heapify(array)
    if count == 0
      @root = Node.new(array.pop)
      @count += 1
    end

    while array != []
      new_node = Node.new(array.pop)
      place_new_node(new_node)
    end
  end

  def clear
    @count = 0
    @root = nil
  end

  def get_list(node=@root)
    return_val = [node.value]
    return_val.concat(get_list(node.left)) if node.left != nil
    return_val.concat(get_list(node.right)) if node.right != nil
    return return_val
  end

  def print
    puts @root.to_s
  end

  def place_new_node(new_node)
    i = @count+1
    current_node = @root

    while i != 1
      if current_node.value < new_node.value
        current_node.value, new_node.value = new_node.value, current_node.value
      end
      if i%2 == 0
        if current_node.left == nil
          current_node.left = new_node
        else
          current_node = current_node.left
        end
      else
        if current_node.right == nil
          current_node.right = new_node
        else
          current_node = current_node.right
        end
      end
      i /= 2
    end

    @count += 1
  end
end

class Node
  attr_accessor :left, :right, :value

  def initialize(value, left = nil, right = nil)
    @value = value
    @left = left
    @right = right
  end

  def to_s
    return "[#{@left? @left.to_s : 'END'} <- #{@value} -> #{@right? @right.to_s : 'END'}]"
  end
end
