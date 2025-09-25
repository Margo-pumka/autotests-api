from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExerciseResponseSchema, ExerciseSchema, \
    UpdateExerciseRequestSchema
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


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: GetExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует данным из ответа создания упражнения.

    :param get_exercise_response: Ответ API при получении упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


def assert_update_exercise_response(
        update_exercise_request: UpdateExerciseRequestSchema,
        update_exercise_response: GetExerciseResponseSchema
):
    """
    Проверяет, что ответ на обновление упражнения соответствует данным из запроса.

    :param update_exercise_request: Исходный запрос на обновление упражнения.
    :param update_exercise_response: Ответ API при обновлении упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(update_exercise_response.exercise.title, update_exercise_request.title,  "title")
    assert_equal(update_exercise_response.exercise.max_score, update_exercise_request.max_score,  "max_score")
    assert_equal(update_exercise_response.exercise.min_score, update_exercise_request.min_score,  "min_score")
    assert_equal(update_exercise_response.exercise.order_index, update_exercise_request.order_index,  "order_index")
    assert_equal(update_exercise_response.exercise.description, update_exercise_request.description,  "description")
    assert_equal(
        update_exercise_response.exercise.estimated_time, update_exercise_request.estimated_time, "estimated_time")

