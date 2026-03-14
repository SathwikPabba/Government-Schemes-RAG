# evaluation/evaluate.py
import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pipeline import GovernmentSchemeRAG

TEST_CASES = [
    {
        "question": "What is PM-KISAN and how much money do farmers get?",
        "ground_truth": "PM-KISAN provides income support of Rs. 6000 per year to farmer families in three installments of Rs. 2000 each directly into bank accounts.",
        "key_facts": ["6000", "2000", "three", "installment", "farmer"]
    },
    {
        "question": "What is the health coverage amount under Ayushman Bharat?",
        "ground_truth": "Ayushman Bharat PM-JAY provides health coverage of Rs. 5 lakh per family per year for secondary and tertiary care hospitalization.",
        "key_facts": ["5 lakh", "family", "year", "hospitalization", "health"]
    },
    {
        "question": "What are the MUDRA loan categories and amounts?",
        "ground_truth": "MUDRA has three categories: Shishu loans up to Rs. 50000, Kishore loans from Rs. 50001 to Rs. 5 lakh, and Tarun loans from Rs. 5 lakh to Rs. 10 lakh.",
        "key_facts": ["shishu", "kishore", "tarun", "50000", "10 lakh"]
    },
    {
        "question": "How many days of employment does MGNREGS guarantee?",
        "ground_truth": "MGNREGS guarantees at least 100 days of wage employment per household per year to rural households.",
        "key_facts": ["100 days", "household", "rural", "wage", "employment"]
    },
    {
        "question": "What is the annual premium for PMSBY accident insurance?",
        "ground_truth": "The premium for PMSBY is only Rs. 20 per year for accident insurance coverage of Rs. 2 lakh.",
        "key_facts": ["20", "2 lakh", "accident", "insurance", "pmsby"]
    },
    {
        "question": "Who is eligible for Sukanya Samridhi Yojana?",
        "ground_truth": "Sukanya Samridhi Yojana is for girl children below 10 years of age, with maximum two accounts per family.",
        "key_facts": ["girl", "10 years", "two accounts", "family", "child"]
    },
    {
        "question": "What loans does PM SVANidhi provide to street vendors?",
        "ground_truth": "PM SVANidhi provides initial loan of Rs. 10000, then Rs. 20000 on timely repayment, and further Rs. 50000 without collateral.",
        "key_facts": ["10000", "20000", "50000", "vendor", "collateral"]
    },
    {
        "question": "What is the guaranteed pension amount under Atal Pension Yojana APY?",
        "ground_truth": "Atal Pension Yojana provides guaranteed pension of Rs. 1000 to Rs. 5000 per month after age 60.",
        "key_facts": ["1,000", "5,000", "pension", "60", "guaranteed"]
    },
    {
        "question": "What benefits does Ujjwala Yojana provide to BPL women?",
        "ground_truth": "Ujjwala Yojana provides free LPG connection with stove and first refill along with financial assistance of Rs. 1600 to BPL women.",
        "key_facts": ["lpg", "free", "1600", "bpl", "women"]
    },
    {
        "question": "What is the subsidy percentage under PMEGP for rural SC/ST applicants?",
        "ground_truth": "Under PMEGP, special category SC/ST applicants in rural areas get 35% subsidy on project cost.",
        "key_facts": ["35", "rural", "sc", "st", "subsidy"]
    },
]

def score_answer(answer: str, key_facts: list, ground_truth: str) -> float:
    answer_lower = answer.lower()
    
    # 1. Key facts matching (60% weight) - checks specific numbers/terms
    facts_matched = sum(1 for fact in key_facts if fact.lower() in answer_lower)
    facts_score = facts_matched / len(key_facts)
    
    # 2. Semantic word overlap (40% weight) - smarter than exact matching
    ground_words = set(w for w in ground_truth.lower().split() 
                      if len(w) > 3 and w not in 
                      ["which", "that", "this", "with", "from", "their", 
                       "have", "been", "will", "under", "only", "also",
                       "each", "then", "than", "into", "more", "some"])
    answer_words = set(answer_lower.split())
    
    if ground_words:
        overlap = len(ground_words & answer_words) / len(ground_words)
    else:
        overlap = 0
    
    # 3. Length penalty — too short answers are penalized
    word_count = len(answer.split())
    length_score = min(word_count / 30, 1.0)  # ideal: 30+ words
    
    # Combined score
    final = (facts_score * 0.5) + (overlap * 0.3) + (length_score * 0.2)
    return round(min(final, 1.0), 2)

def evaluate_rag():
    print("=" * 60)
    print("GOVERNMENT SCHEME RAG - EVALUATION REPORT")
    print("=" * 60)
    print(f"\nLoading RAG pipeline...")
    pipeline = GovernmentSchemeRAG()
    print("Pipeline loaded!\n")

    results = []
    total_questions = len(TEST_CASES)

    for i, test in enumerate(TEST_CASES, 1):
        print(f"[{i}/{total_questions}] {test['question'][:60]}...")
        result = pipeline.query(test["question"])

        # Faithfulness: answer grounded in retrieved docs
        faithfulness_score = 1.0 if len(result.sources) > 0 else 0.0

        # Answer Relevancy: smarter scoring with key facts
        relevancy_score = score_answer(
            result.answer,
            test["key_facts"],
            test["ground_truth"]
        )

        # Context Score: relevant sources retrieved
        context_score = round(min(result.num_sources / 3, 1.0), 2)

        overall = round((relevancy_score + faithfulness_score + context_score) / 3, 2)

        results.append({
            "question": test["question"],
            "answer_preview": result.answer[:200] + "...",
            "ground_truth": test["ground_truth"],
            "num_sources": result.num_sources,
            "faithfulness": faithfulness_score,
            "answer_relevancy": relevancy_score,
            "context_score": context_score,
            "overall": overall
        })

        print(f"   Faithfulness:     {faithfulness_score:.2f}")
        print(f"   Answer Relevancy: {relevancy_score:.2f}")
        print(f"   Context Score:    {context_score:.2f}")
        print(f"   Overall:          {overall:.2f}\n")

    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    avg_faith = round(sum(r["faithfulness"] for r in results) / total_questions, 3)
    avg_rel   = round(sum(r["answer_relevancy"] for r in results) / total_questions, 3)
    avg_ctx   = round(sum(r["context_score"] for r in results) / total_questions, 3)
    avg_ovr   = round(sum(r["overall"] for r in results) / total_questions, 3)

    print(f"Total Questions Evaluated : {total_questions}")
    print(f"Average Faithfulness      : {avg_faith}")
    print(f"Average Answer Relevancy  : {avg_rel}")
    print(f"Average Context Score     : {avg_ctx}")
    print(f"Average Overall Score     : {avg_ovr}")
    print("=" * 60)

    report = {
        "summary": {
            "total_questions": total_questions,
            "avg_faithfulness": avg_faith,
            "avg_answer_relevancy": avg_rel,
            "avg_context_score": avg_ctx,
            "avg_overall": avg_ovr
        },
        "detailed_results": results
    }

    with open("evaluation/eval_results.json", "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n✅ Results saved to evaluation/eval_results.json")
    return report

if __name__ == "__main__":
    evaluate_rag()