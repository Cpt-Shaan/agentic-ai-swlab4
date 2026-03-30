from planner import generate_plan
from tools import extract_numbers, compute_average, summarize_result


class PlanningAgent:
    def run(self, query):
        print("\nGenerating plan...\n")
        plan = generate_plan(query)
        print("Plan Steps:")
        for step in plan:
            print("-", step)
        data = None
        print("\nExecuting steps...\n")
        
        for step in plan:
            if step == "extract_numbers":
                data = extract_numbers(query)
                print("Step: Extract Numbers")
                print("Numbers:", data, "\n")
            elif step == "compute_average":
                data = compute_average(data)
                print("Step: Compute Average")
                print("Average:", data, "\n")
            elif step == "summarize_result":
                summary = summarize_result(data)
                print("Step: Summarize Result")
                print("Summary:", summary, "\n")
                return summary

        return data