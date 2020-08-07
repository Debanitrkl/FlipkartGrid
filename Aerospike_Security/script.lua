local function unmarshallToTargetedCard(pb_bytes)
  local grid_pb = require "grid_pb"
  local pb_data = bytes.get_string(pb_bytes, 1, bytes.size(pb_bytes))
  local msg = grid_pb.Shop_Processed()
  msg:ParseFromString(pb_data)
  return msg
end

local function isCardExpired(msg)
  local nowTimestamp = os.time(os.date('*t'))
  if(msg.end_time<nowTimestamp and msg.end_time ~= -1) then
    return true
  else
    return false
  end
end

local function deleteBin(rec,binname)
  rec[binname] = nil
  aerospike:update(rec)
end

function clean_record(rec)
  names = record.bin_names(rec)
  for i, name in ipairs(names) do
    local binname = tostring(name)
    pb_bytes = rec[binname]
    local success,msg = pcall(unmarshallToTargetedCard, pb_bytes)
    if not success then
      error(msg)
    end
    if(isCardExpired(msg))
    then
      deleteBin(rec,binname)
    end
  end
end
