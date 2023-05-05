from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CLOSED: CodeType
CODE_TYPE_UNSPECIFIED: CodeType
DESCRIPTOR: _descriptor.FileDescriptor
WARNING: CodeType
WORKING: CodeType

class Alternative(_message.Message):
    __slots__ = ["confidence", "end_time_ms", "languages", "start_time_ms", "text", "words"]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    confidence: float
    end_time_ms: int
    languages: _containers.RepeatedCompositeFieldContainer[LanguageEstimation]
    start_time_ms: int
    text: str
    words: _containers.RepeatedCompositeFieldContainer[Word]
    def __init__(self, words: _Optional[_Iterable[_Union[Word, _Mapping]]] = ..., text: _Optional[str] = ..., start_time_ms: _Optional[int] = ..., end_time_ms: _Optional[int] = ..., confidence: _Optional[float] = ..., languages: _Optional[_Iterable[_Union[LanguageEstimation, _Mapping]]] = ...) -> None: ...

class AlternativeUpdate(_message.Message):
    __slots__ = ["alternatives", "channel_tag"]
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TAG_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[Alternative]
    channel_tag: str
    def __init__(self, alternatives: _Optional[_Iterable[_Union[Alternative, _Mapping]]] = ..., channel_tag: _Optional[str] = ...) -> None: ...

class AudioChunk(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class AudioCursors(_message.Message):
    __slots__ = ["eou_time_ms", "final_index", "final_time_ms", "partial_time_ms", "received_data_ms", "reset_time_ms"]
    EOU_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FINAL_INDEX_FIELD_NUMBER: _ClassVar[int]
    FINAL_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_DATA_MS_FIELD_NUMBER: _ClassVar[int]
    RESET_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    eou_time_ms: int
    final_index: int
    final_time_ms: int
    partial_time_ms: int
    received_data_ms: int
    reset_time_ms: int
    def __init__(self, received_data_ms: _Optional[int] = ..., reset_time_ms: _Optional[int] = ..., partial_time_ms: _Optional[int] = ..., final_time_ms: _Optional[int] = ..., final_index: _Optional[int] = ..., eou_time_ms: _Optional[int] = ...) -> None: ...

class AudioFormatOptions(_message.Message):
    __slots__ = ["container_audio", "raw_audio"]
    CONTAINER_AUDIO_FIELD_NUMBER: _ClassVar[int]
    RAW_AUDIO_FIELD_NUMBER: _ClassVar[int]
    container_audio: ContainerAudio
    raw_audio: RawAudio
    def __init__(self, raw_audio: _Optional[_Union[RawAudio, _Mapping]] = ..., container_audio: _Optional[_Union[ContainerAudio, _Mapping]] = ...) -> None: ...

class ContainerAudio(_message.Message):
    __slots__ = ["container_audio_type"]
    class ContainerAudioType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONTAINER_AUDIO_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_AUDIO_TYPE_UNSPECIFIED: ContainerAudio.ContainerAudioType
    MP3: ContainerAudio.ContainerAudioType
    OGG_OPUS: ContainerAudio.ContainerAudioType
    WAV: ContainerAudio.ContainerAudioType
    container_audio_type: ContainerAudio.ContainerAudioType
    def __init__(self, container_audio_type: _Optional[_Union[ContainerAudio.ContainerAudioType, str]] = ...) -> None: ...

class DefaultEouClassifier(_message.Message):
    __slots__ = ["max_pause_between_words_hint_ms", "type"]
    class EouSensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DEFAULT: DefaultEouClassifier.EouSensitivity
    EOU_SENSITIVITY_UNSPECIFIED: DefaultEouClassifier.EouSensitivity
    HIGH: DefaultEouClassifier.EouSensitivity
    MAX_PAUSE_BETWEEN_WORDS_HINT_MS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    max_pause_between_words_hint_ms: int
    type: DefaultEouClassifier.EouSensitivity
    def __init__(self, type: _Optional[_Union[DefaultEouClassifier.EouSensitivity, str]] = ..., max_pause_between_words_hint_ms: _Optional[int] = ...) -> None: ...

class Eou(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EouClassifierOptions(_message.Message):
    __slots__ = ["default_classifier", "external_classifier"]
    DEFAULT_CLASSIFIER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CLASSIFIER_FIELD_NUMBER: _ClassVar[int]
    default_classifier: DefaultEouClassifier
    external_classifier: ExternalEouClassifier
    def __init__(self, default_classifier: _Optional[_Union[DefaultEouClassifier, _Mapping]] = ..., external_classifier: _Optional[_Union[ExternalEouClassifier, _Mapping]] = ...) -> None: ...

class EouUpdate(_message.Message):
    __slots__ = ["time_ms"]
    TIME_MS_FIELD_NUMBER: _ClassVar[int]
    time_ms: int
    def __init__(self, time_ms: _Optional[int] = ...) -> None: ...

class ExternalEouClassifier(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinalRefinement(_message.Message):
    __slots__ = ["final_index", "normalized_text"]
    FINAL_INDEX_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_TEXT_FIELD_NUMBER: _ClassVar[int]
    final_index: int
    normalized_text: AlternativeUpdate
    def __init__(self, final_index: _Optional[int] = ..., normalized_text: _Optional[_Union[AlternativeUpdate, _Mapping]] = ...) -> None: ...

class LanguageEstimation(_message.Message):
    __slots__ = ["language_code", "probability"]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    probability: float
    def __init__(self, language_code: _Optional[str] = ..., probability: _Optional[float] = ...) -> None: ...

class LanguageRestrictionOptions(_message.Message):
    __slots__ = ["language_code", "restriction_type"]
    class LanguageRestrictionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BLACKLIST: LanguageRestrictionOptions.LanguageRestrictionType
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_RESTRICTION_TYPE_UNSPECIFIED: LanguageRestrictionOptions.LanguageRestrictionType
    RESTRICTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    WHITELIST: LanguageRestrictionOptions.LanguageRestrictionType
    language_code: _containers.RepeatedScalarFieldContainer[str]
    restriction_type: LanguageRestrictionOptions.LanguageRestrictionType
    def __init__(self, restriction_type: _Optional[_Union[LanguageRestrictionOptions.LanguageRestrictionType, str]] = ..., language_code: _Optional[_Iterable[str]] = ...) -> None: ...

class RawAudio(_message.Message):
    __slots__ = ["audio_channel_count", "audio_encoding", "sample_rate_hertz"]
    class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUDIO_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ENCODING_UNSPECIFIED: RawAudio.AudioEncoding
    LINEAR16_PCM: RawAudio.AudioEncoding
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    audio_channel_count: int
    audio_encoding: RawAudio.AudioEncoding
    sample_rate_hertz: int
    def __init__(self, audio_encoding: _Optional[_Union[RawAudio.AudioEncoding, str]] = ..., sample_rate_hertz: _Optional[int] = ..., audio_channel_count: _Optional[int] = ...) -> None: ...

class RecognitionModelOptions(_message.Message):
    __slots__ = ["audio_format", "audio_processing_type", "language_restriction", "model", "text_normalization"]
    class AudioProcessingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_PROCESSING_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_PROCESSING_TYPE_UNSPECIFIED: RecognitionModelOptions.AudioProcessingType
    FULL_DATA: RecognitionModelOptions.AudioProcessingType
    LANGUAGE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    REAL_TIME: RecognitionModelOptions.AudioProcessingType
    TEXT_NORMALIZATION_FIELD_NUMBER: _ClassVar[int]
    audio_format: AudioFormatOptions
    audio_processing_type: RecognitionModelOptions.AudioProcessingType
    language_restriction: LanguageRestrictionOptions
    model: str
    text_normalization: TextNormalizationOptions
    def __init__(self, model: _Optional[str] = ..., audio_format: _Optional[_Union[AudioFormatOptions, _Mapping]] = ..., text_normalization: _Optional[_Union[TextNormalizationOptions, _Mapping]] = ..., language_restriction: _Optional[_Union[LanguageRestrictionOptions, _Mapping]] = ..., audio_processing_type: _Optional[_Union[RecognitionModelOptions.AudioProcessingType, str]] = ...) -> None: ...

class SessionUuid(_message.Message):
    __slots__ = ["user_request_id", "uuid"]
    USER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    user_request_id: str
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., user_request_id: _Optional[str] = ...) -> None: ...

class SilenceChunk(_message.Message):
    __slots__ = ["duration_ms"]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    duration_ms: int
    def __init__(self, duration_ms: _Optional[int] = ...) -> None: ...

class StatusCode(_message.Message):
    __slots__ = ["code_type", "message"]
    CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code_type: CodeType
    message: str
    def __init__(self, code_type: _Optional[_Union[CodeType, str]] = ..., message: _Optional[str] = ...) -> None: ...

class StreamingOptions(_message.Message):
    __slots__ = ["eou_classifier", "recognition_model"]
    EOU_CLASSIFIER_FIELD_NUMBER: _ClassVar[int]
    RECOGNITION_MODEL_FIELD_NUMBER: _ClassVar[int]
    eou_classifier: EouClassifierOptions
    recognition_model: RecognitionModelOptions
    def __init__(self, recognition_model: _Optional[_Union[RecognitionModelOptions, _Mapping]] = ..., eou_classifier: _Optional[_Union[EouClassifierOptions, _Mapping]] = ...) -> None: ...

class StreamingRequest(_message.Message):
    __slots__ = ["chunk", "eou", "session_options", "silence_chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    EOU_FIELD_NUMBER: _ClassVar[int]
    SESSION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SILENCE_CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: AudioChunk
    eou: Eou
    session_options: StreamingOptions
    silence_chunk: SilenceChunk
    def __init__(self, session_options: _Optional[_Union[StreamingOptions, _Mapping]] = ..., chunk: _Optional[_Union[AudioChunk, _Mapping]] = ..., silence_chunk: _Optional[_Union[SilenceChunk, _Mapping]] = ..., eou: _Optional[_Union[Eou, _Mapping]] = ...) -> None: ...

class StreamingResponse(_message.Message):
    __slots__ = ["audio_cursors", "eou_update", "final", "final_refinement", "partial", "response_wall_time_ms", "session_uuid", "status_code"]
    AUDIO_CURSORS_FIELD_NUMBER: _ClassVar[int]
    EOU_UPDATE_FIELD_NUMBER: _ClassVar[int]
    FINAL_FIELD_NUMBER: _ClassVar[int]
    FINAL_REFINEMENT_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_WALL_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SESSION_UUID_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    audio_cursors: AudioCursors
    eou_update: EouUpdate
    final: AlternativeUpdate
    final_refinement: FinalRefinement
    partial: AlternativeUpdate
    response_wall_time_ms: int
    session_uuid: SessionUuid
    status_code: StatusCode
    def __init__(self, session_uuid: _Optional[_Union[SessionUuid, _Mapping]] = ..., audio_cursors: _Optional[_Union[AudioCursors, _Mapping]] = ..., response_wall_time_ms: _Optional[int] = ..., partial: _Optional[_Union[AlternativeUpdate, _Mapping]] = ..., final: _Optional[_Union[AlternativeUpdate, _Mapping]] = ..., eou_update: _Optional[_Union[EouUpdate, _Mapping]] = ..., final_refinement: _Optional[_Union[FinalRefinement, _Mapping]] = ..., status_code: _Optional[_Union[StatusCode, _Mapping]] = ...) -> None: ...

class TextNormalizationOptions(_message.Message):
    __slots__ = ["literature_text", "phone_formatting_mode", "profanity_filter", "text_normalization"]
    class PhoneFormattingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class TextNormalization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    LITERATURE_TEXT_FIELD_NUMBER: _ClassVar[int]
    PHONE_FORMATTING_MODE_DISABLED: TextNormalizationOptions.PhoneFormattingMode
    PHONE_FORMATTING_MODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FORMATTING_MODE_UNSPECIFIED: TextNormalizationOptions.PhoneFormattingMode
    PROFANITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    TEXT_NORMALIZATION_DISABLED: TextNormalizationOptions.TextNormalization
    TEXT_NORMALIZATION_ENABLED: TextNormalizationOptions.TextNormalization
    TEXT_NORMALIZATION_FIELD_NUMBER: _ClassVar[int]
    TEXT_NORMALIZATION_UNSPECIFIED: TextNormalizationOptions.TextNormalization
    literature_text: bool
    phone_formatting_mode: TextNormalizationOptions.PhoneFormattingMode
    profanity_filter: bool
    text_normalization: TextNormalizationOptions.TextNormalization
    def __init__(self, text_normalization: _Optional[_Union[TextNormalizationOptions.TextNormalization, str]] = ..., profanity_filter: bool = ..., literature_text: bool = ..., phone_formatting_mode: _Optional[_Union[TextNormalizationOptions.PhoneFormattingMode, str]] = ...) -> None: ...

class Word(_message.Message):
    __slots__ = ["end_time_ms", "start_time_ms", "text"]
    END_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    end_time_ms: int
    start_time_ms: int
    text: str
    def __init__(self, text: _Optional[str] = ..., start_time_ms: _Optional[int] = ..., end_time_ms: _Optional[int] = ...) -> None: ...

class CodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
