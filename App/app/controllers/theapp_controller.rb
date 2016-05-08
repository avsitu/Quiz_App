class TheappController < ApplicationController
  def index
  	r = Random.new
  	@mquestions = Array.new
  	@squestions = Array.new
    for n in 0...100
  		i = r.rand(1...400)
  		q = Question.find(i)
  		@mquestions << q 
  		j = r.rand(401...765)
  		s = Question.find(j)
  		@squestions << s
  	end	
  end
end
