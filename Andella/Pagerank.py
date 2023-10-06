import os
import networkx as nx

##in this challenge you will write a function simple_pagerank(directory) and use networkx's pagerank function to compute thepage ranking

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
            G.add_nodes_from([file])
            #print(f"file:{file} link {links} " )
            G.add_edges_from(((file, link) for link in links))
            #G.add_edges_from((file, links))

    # Compute PageRank using NetworkX
   
    print("Nodes================================")
    print(G.nodes)
    print(list(G.nodes(data=True)))
    print("Graph================================")
    pagerank_scores = nx.pagerank(G)
    # print("Graph================================")
    # print(G.graph)
    # print(list(G.nodes(data=True)))
    # print("Graph================================")
    # print(pagerank_scores.keys())
  
    #print (pagerank_scores)

    # Print the PageRank scores
    # print("PageRank Scores:")
    # for node, score in pagerank_scores.items():
    #     print(f"{node}: {score}")

    print("PageRank Scores for Each Page:")
    for page, score in pagerank_scores.items():
        #if ".html" in page:
        print(f"Page= {page}: Score {score}")


    # overall_rank = sorted(pagerank_scores, key=pagerank_scores.get, reverse=True)
    # print("\nOverall Rank Based on Total PageRank Scores:")
    # for file in overall_rank:
    #     print(f"{file}: {pagerank_scores[file]}")

   # print("add_edges_from ",pagerank_scores[0])
    # print(dir(pagerank_scores),type(pagerank_scores))
    sorted_nodes = sorted([(node, pagerank) for node, pagerank in pagerank_scores.items()], key=lambda x:pagerank_scores[x[0]])
    print("Sorted Nodes:",sorted_nodes)
    print("Added edges from")
    for node in sorted_nodes:
        if node[0].endswith(".html"):
            print (node)


# Example usage
simple_pagerank("samplepages")


def simple_pagerank2(directory):
    # Create a directed graph
    graph = nx.DiGraph()

    # Iterate over files in the specified directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Read the contents of the file and split into words
        with open(filepath, 'r', encoding='utf-8') as file:
            words = file.read().split()

        # Add edges to the graph based on word pairs
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            graph.add_edge(word1, word2)

    # Use networkx's pagerank function to compute pagerank values
    pagerank_values = nx.pagerank(graph)
    print(pagerank_values)
    print("\n================================")
    word_scores = {}
    for word in pagerank_values:
        word_scores[word] = pagerank_values[word]

    return word_scores


    r#eturn pagerank_values

# Example usage
# directory_path = 'samplepages'
# pagerank_result = simple_pagerank2(directory_path)

# # Print the PageRank values
# print("################################ 2 ############################# ")
# for node, score in pagerank_result.items():
#     print(f'{node}: {score}')