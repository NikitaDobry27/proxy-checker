import requests
import concurrent.futures



def make_request(url, proxy):

  try:
    response = requests.get(url, proxies={"http": proxy, "https": proxy})
  except requests.exceptions.ProxyError as e:
   
    print("Proxy error occurred for proxy {}: {}. Continuing to next proxy...".format(proxy, e))
    return None
  else:
   
    return response.text


url = "https://checker.soax.com/api/ipinfo"


proxies = ["http://YT7fBfPlVx5S09VH:wifi;at;;styria;@proxy.soax.com:{}".format(port) for port in range(9000, 9000 + int(input("Insert desired number of port: ")))]


with concurrent.futures.ThreadPoolExecutor() as executor:
  
  results = executor.map(lambda p: make_request(url, p), proxies)


  results = [result for result in results if result is not None]

  result_counts = {}
  for result in results:
    if result in result_counts:
      result_counts[result] += 1
    else:
      result_counts[result] = 1
  
  uniq_results_count = 0
  for result, count in result_counts.items():
    if count >= 1:
      uniq_results_count += 1
    
  duplicated_results = len(results) - uniq_results_count
  
  
  for result, count in result_counts.items():
    print("{}: {}".format(result, count))
  print("Total requests: {}".format(len(results)))
  print("Uniq IPs: {}".format(uniq_results_count))
  print("Duplicated IPs: {}".format(duplicated_results))