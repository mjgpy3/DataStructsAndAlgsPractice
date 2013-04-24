class MathList
  def initialize
    @sum = 0
    @prod = 1
    @counts = {}
    @items = []
  end

  def add item
    @sum += item
    @prod *= item
    
    if @counts.include? item
      @counts[item] += 1
    else
      @counts[item] = 1
    end

    @items << item
  end

  def remove item
    if not @items.find_index(item) == nil
      @sum -= item
      @prod /= item
      @counts[item] -= 1

      @counts[item] = nil if @counts[item] <= 0
      @items.delete_at(@items.find_index item)
    end
  end

  def to_a
    @items.collect {|x| x}
  end

  def sum
    @sum
  end

  def prod
    @prod
  end

  def count item
    if @counts.include? item
      if not @counts[item] == nil
        return @counts[item]
      end
    end

    return 0
  end

  def length
    @items.count
  end
end
