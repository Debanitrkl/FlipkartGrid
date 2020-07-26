function put_data(rec, Colour, Discount, Ratings_count, Price, Ratings, Score)
  local grid_pb = require "grid_pb"
  -- Serialize Example
  local msg = grid_pb.Shop_Processed()
  msg.Colour = Colour
  msg.Discount = Discount
  msg.Ratings_count = Ratings_count
  msg.Price = Price
  msg.Ratings = Ratings
  msg.Score = Score
  local pb_data = msg:SerializeToString()
  local pb_bytes = bytes(pb_data:len())
  bytes.set_type(pb_bytes, 4)
  bytes.set_string(pb_bytes, 1, pb_data)
  rec["product_details"] = pb_bytes
  if aerospike:exists(rec) then
    aerospike:update(rec)
  else
    aerospike:create(rec)
  end
end

function verify_data(rec)
  local grid_pb = require "grid_pb"
  -- Parse Example
  local pb_bytes = rec["product_details"]
  local pb_data = bytes.get_string(pb_bytes, 1, bytes.size(pb_bytes))
  local msg = grid_pb.Shop_Processed()
  msg:ParseFromString(pb_data)
  local returnMap = map()
  returnMap.Colour = msg.Colour
  returnMap.Discount = msg.Discount
  returnMap.Ratings_count = msg.Ratings_count
  returnMap.Price = msg.Price
  returnMap.Ratings = msg.Ratings
  returnMap.Score = msg.Score
  return returnMap
end
