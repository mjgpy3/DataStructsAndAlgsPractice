require './math_list'
require 'test/unit'

class TestMathList < Test::Unit::TestCase

  def test_after_adding_a_few_items_data_are_consistient
    ml = MathList.new

    ml.add 5
    ml.add 7
    ml.add -4

    assert_a_list_with_5_7_and_negative_4 ml
  end

  def test_removing_items_that_do_not_exits_doesnt_do_anything
    ml = MathList.new

    ml.add 5
    ml.add 7
    ml.add -4

    ml.remove 1

    assert_a_list_with_5_7_and_negative_4 ml
  end

  def test_removing_an_item_behaves_expectedly
    ml = MathList.new

    ml.add 5
    ml.add 7
    ml.add -4
    ml.remove -4

    assert_a_list_with_5_7 ml
  end

  def assert_a_list_with_5_7_and_negative_4 ml
    assert_equal 8, ml.sum
    assert_equal -140, ml.prod
    assert_equal [5, 7, -4], ml.to_a
    assert_equal 1, ml.count(5)
    assert_equal 1, ml.count(7)
    assert_equal 1, ml.count(-4)
    assert_equal 0, ml.count(23)
    assert_equal 3, ml.length
  end

  def assert_a_list_with_5_7 ml
    assert_equal 12, ml.sum
    assert_equal 35, ml.prod
    assert_equal [5, 7], ml.to_a
    assert_equal 1, ml.count(5)
    assert_equal 1, ml.count(7)
    assert_equal 0, ml.count(-4)
    assert_equal 0, ml.count(23)
    assert_equal 2, ml.length
  end
end
