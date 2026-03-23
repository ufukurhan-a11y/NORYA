from datetime import datetime

from sqlmodel import Field, SQLModel


class AuditLog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    event: str = Field(index=True)  # login, register, analyze, case_create, case_review, invite_send, etc.
    user_id: int | None = Field(default=None, index=True)
    ip: str | None = None
    country: str | None = None
    city: str | None = None
    institution_id: int | None = Field(default=None, index=True)
    entity_type: str | None = Field(default=None, max_length=64)  # case, report, membership, institution
    entity_id: int | None = Field(default=None)
    metadata_json: str | None = None  # JSON string for extra context
    created_at: datetime = Field(default_factory=datetime.utcnow)
