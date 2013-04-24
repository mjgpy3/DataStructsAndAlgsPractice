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
      return @counts[item]
    else
      return 0
    end
  end
end
