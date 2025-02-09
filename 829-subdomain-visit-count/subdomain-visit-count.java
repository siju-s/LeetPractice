class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> count = new HashMap<>();

        for (String domain: cpdomains) {
            int index = domain.indexOf(" ");
            int freq = Integer.parseInt(domain.substring(0, index));
            String root = domain.substring(index + 1, domain.length());
            System.out.println(root);

            count.put(root, count.getOrDefault(root, 0) + freq);
            
            int index1 = root.indexOf(".");
            if (index1 != -1) {
                String root2 = root.substring(index1 + 1, root.length());
                System.out.println("Root2:"+root2);
                count.put(root2, count.getOrDefault(root2, 0) + freq);
                
                int index2 = root2.indexOf(".");
                if (index2 != -1) {
                    String root3 = root2.substring(index2 + 1, root2.length());
                    System.out.println("Root3:"+root3);
                    count.put(root3, count.getOrDefault(root3, 0) + freq);
                    
                }
                
            }

                
            }

            List<String> output = new ArrayList<>();
            Iterator<Map.Entry<String, Integer>> iterator = count.entrySet().iterator(); 
            while (iterator.hasNext()) {
                Map.Entry<String,Integer> entry = iterator.next();
                String key = entry.getKey();
                int value = entry.getValue();

                output.add(value + " " + key);
            }

            return output;
        }
        
    }
