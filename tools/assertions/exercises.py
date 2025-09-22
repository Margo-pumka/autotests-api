from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(
        create_exercise_request: CreateExerciseRequestSchema,
        create_exercise_response: GetExerciseResponseSchema):
    """
    Проверяет, что ответ на создание упражнения соответствует данным из запроса.

    :param create_exercise_request: Исходный запрос на создание упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(create_exercise_request.title, create_exercise_response.exercise.title, "title")
    assert_equal(create_exercise_request.course_id, create_exercise_response.exercise.course_id, "course_id")
    assert_equal(create_exercise_request.max_score, create_exercise_response.exercise.max_score, "max_score")
    assert_equal(create_exercise_request.min_score, create_exercise_response.exercise.min_score, "min_score")
    assert_equal(create_exercise_request.order_index, create_exercise_response.exercise.order_index, "order_index")
    assert_equal(create_exercise_request.description, create_exercise_response.exercise.description, "description")
    assert_equal(create_exercise_request.estimated_time, create_exercise_response.exercise.estimated_time, "estimated_time")
