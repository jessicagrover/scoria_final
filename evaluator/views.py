import openai
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EvaluationSerializer

# Set your OpenAI API key
openai.api_key = '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'

# Set up logging
logger = logging.getLogger(__name__)

class EvaluateAnswerView(APIView):
    def post(self, request):
        serializer = EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            question_text = serializer.validated_data['question_text']
            answer_text = serializer.validated_data['answer_text']
            try:
                prompt = f"Given the Question: {question_text}\n\nAnd the answer text: {answer_text}\n\nProvide only the score in percentage for the answer without any explanation. Just the numeric value."

                response = openai.ChatCompletion.create(
                    model='gpt-4-turbo',
                    messages=[
                        {'role': 'system', 'content': 'You are an expert professor scoring based on the questions and answers.'},
                        {'role': 'user', 'content': prompt}
                    ],
                    max_tokens=50,  # Reduced to ensure we only get the score
                    temperature=0.7
                )

                completion_text = response.choices[0].message['content']
                # Extract only the numeric value (assumes the response is just the score)
                score_str = completion_text.strip()
                return Response({"score": score_str}, status=status.HTTP_200_OK)
            except openai.error.OpenAIError as e:
                logger.error(f"OpenAI API error: {e}")
                return Response({"error": "OpenAI API error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                return Response({"error": "An error occurred while processing the request"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
