class TheappController < ApplicationController
  def index
  	r = Random.new
  	@questions = Array.new
    for n in 0...100
  		i = r.rand(400...500)
  		@questions << Question.find(i)  
  	end	
  end
end
