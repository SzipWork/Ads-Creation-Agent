from langgraph.graph import StateGraph
from app.graph.state import AdState
from app.graph.nodes import (
    intent_extraction_node,
    oauth_node,
    business_rule_node,
    music_validation_node,
    submission_node
)


def build_graph():
    graph = StateGraph(AdState)

    graph.add_node("intent", intent_extraction_node)
    graph.add_node("oauth", oauth_node)
    graph.add_node("rules", business_rule_node)
    graph.add_node("music", music_validation_node)
    graph.add_node("submit", submission_node)

    graph.set_entry_point("intent")
    graph.add_edge("intent", "oauth")
    graph.add_edge("oauth", "rules")
    graph.add_edge("rules", "music")
    graph.add_edge("music", "submit")

    return graph.compile()
