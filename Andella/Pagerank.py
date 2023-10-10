import os
import networkx as nx
from bs4 import BeautifulSoup
##in this challenge you will write a function simple_pagerank(directory) and use networkx's pagerank function to compute thepage ranking

          
def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract relevant data using BeautifulSoup methods
    # Modify this part based on the structure of the HTML on the webpage
    title = soup.title.text if soup.title else "No Title"
    content = soup.find('body').text.strip() if soup.find('body') else "No Content"
    href = soup.find('a') .get("href") if soup.find('a') else ""
    d= {'title': title, 'content': content,"href":href}
    #print("result",d)
    return d

def simple_pagerankV2(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Get a list of files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Create a directed graph using NetworkX
    G = nx.DiGraph()
    files_link=[]
    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            links=f.read()
            read_data=extract_data(links)
            #print("FIle ",file," Data ",read_data)
            G.add_node(file, **read_data)

            #G.add_node(file)
            files_link.append((file,read_data['href'],{"type": "navigation"}))
            
    G.add_edges_from(files_link)

    page_rank_scores = nx.pagerank(G)


    # Print or use PageRank scores and attributes for each webpage
    for webpage, score in page_rank_scores.items():
        attributes = G.nodes[webpage]
        print(f"Webpage {webpage} (Score: {score}): {attributes}")

    print("Result Dict ",page_rank_scores,type(page_rank_scores))
      
simple_pagerankV2("samplepages")

def simple_pagerank(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Get a list of files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Create a directed graph using NetworkX
    G = nx.DiGraph()

    # Populate the graph based on links in the files
    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            # For simplicity, let's assume that each line in a file represents a link
            links = [line.strip() for line in f.readlines()]
            #G.add_node(file)
            
            #print(f"file:{file} link {links} " )
            G.add_edges_from(((file, link) for link in links))

            #G.add_nodes_from([file])
           
    # Compute PageRank using NetworkX
   
    # print("Nodes================================")
    # print(G.nodes)
    # print(list(G.nodes(data=True)))
    # print("Graph================================")


    pagerank_scores = nx.pagerank(G)
    #alpha=0.85, nstart={'A': 0, 'B': 0, 'C': 1, 'D': 0}

   

    #pagerank_scores2 = nx.pagerank(G, personalization={'aa.html': 0, 'bb.html': 0, 'cc.html': 0})

    # print("Graph================================")
    # print(G.graph)
    # print(list(G.nodes(data=True)))
    # print("Graph================================")
    # print(pagerank_scores.keys())
  
    # print("pagerank_scores2 == pagerank_scores2")
    # print (pagerank_scores2)
    # print("pagerank_scores2 == pagerank_scores2")

    # Print the PageRank scores
    # print("PageRank Scores:")
    # for node, score in pagerank_scores.items():
    #     print(f"{node}: {score}")

    print("PageRank Scores for Each Page:")
    for page, score in pagerank_scores.items():
        #if ".html" in page:
        print(f"Page= {page}: Score {score}")

    G.add_nodes_from(files)
    # Create a subgraph containing only the new nodes
    new_nodes_graph = G.subgraph(files)

    # Compute PageRank for the new nodes
    new_nodes_page_rank_scores = nx.pagerank(new_nodes_graph)

    for node, score in new_nodes_page_rank_scores.items():
        print(f"Node {node}: {score}")




    # overall_rank = sorted(pagerank_scores, key=pagerank_scores.get, reverse=True)
    # print("\nOverall Rank Based on Total PageRank Scores:")
    # for file in overall_rank:
    #     print(f"{file}: {pagerank_scores[file]}")

   # print("add_edges_from ",pagerank_scores[0])
    # print(dir(pagerank_scores),type(pagerank_scores))
    # sorted_nodes = sorted([(node, pagerank) for node, pagerank in pagerank_scores.items()], key=lambda x:pagerank_scores[x[0]])
    # print("Sorted Nodes:",sorted_nodes)
    # print("Added edges from")
    # result={}
    # for node in sorted_nodes:
    #     if node[0].endswith(".html"):
    #         print (node)
    #         result[node[0]] = node[1]
    #     elif '.html' in node[0]:
    #         print("Node check eslse ",node[0])
    #         for kk in result.keys():
    #             if kk in node[0]:
    #                 result[kk]=result[kk]+node[1]
    #             else:
    #                 print("Not kk in node[0] ",kk,node[0])
    # print(result)

  



def sample_followed():
    print(" ##New## "*7)

    G = nx.DiGraph()

    # Add webpages and links
    webpages_and_links = [
        ("home", "about"),
        ("home", "contact"),
        ("about", "services"),
        ("services", "contact"),
        ("contact", "home"),
    ]

    G.add_edges_from(webpages_and_links)

    # Compute PageRank scores
    page_rank_scores = nx.pagerank(G)

    # Print or use PageRank scores for each webpage
    for webpage, score in page_rank_scores.items():
        print(f"Webpage {webpage}: {score}")


def other_pages():

    # Create a directed graph
    G = nx.DiGraph()

    # Add webpages with attributes
    webpages_with_attributes = {
        "home": {"title": "Home Page", "content": "Welcome to our website."},
        "about": {"title": "About Us", "content": "Learn more about our company."},
        "contact": {"title": "Contact Us", "content": "Get in touch with us."},
        "services": {"title": "Our Services", "content": "Explore our offered services."},
    }

    G.add_nodes_from(webpages_with_attributes.items())

    # Add links with attributes
    webpage_links_with_attributes = [
        ("home", "about", {"type": "navigation"}),
        ("home", "contact", {"type": "navigation"}),
        ("about", "services", {"type": "navigation"}),
        ("services", "contact", {"type": "navigation"}),
        ("contact", "home", {"type": "navigation"}),
    ]

    G.add_edges_from(webpage_links_with_attributes)

    # Compute PageRank scores
    page_rank_scores = nx.pagerank(G)

    # Print or use PageRank scores and attributes for each webpage
    for webpage, score in page_rank_scores.items():
        attributes = G.nodes[webpage]
        print(f"Webpage {webpage} (Score: {score}): {attributes}")

#print("other_pages()")
#other_pages()