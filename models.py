from sqlalchemy import (
    Column, Integer, String, Text, Numeric, Date, Boolean, 
    DateTime, BigInteger, func, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

Base = declarative_base()

class Contribution(Base):
    __tablename__ = 'contributions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    jurisdiction = Column(Text, nullable=False)
    source_system = Column(Text, nullable=False)
    contributor_name = Column(Text)
    contributor_type = Column(Text)
    recipient_name = Column(Text)
    recipient_id = Column(Text)
    amount = Column(Numeric)
    date = Column(Date)
    office = Column(Text)
    race = Column(Text)
    party = Column(Text)
    raw_source_url = Column(Text)
    raw_record = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class IlContractualLobbyist(Base):
    __tablename__ = 'il_contractual_lobbyists'

    il_contractual_pk = Column(Text, primary_key=True)
    ent_reg_year = Column(Integer)
    entity_id = Column(Text)
    entity_name = Column(Text)
    contractual_id = Column(Text)
    contractual_name = Column(Text)
    source_row_id = Column(Text)
    source_created_at = Column(DateTime(timezone=True))
    source_updated_at = Column(DateTime(timezone=True))
    batch_id = Column(Text)
    raw_json = Column(JSONB)
    inserted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

class IlEntity(Base):
    __tablename__ = 'il_entities'

    il_entities_pk = Column(Text, primary_key=True)
    ent_reg_year = Column(Integer)
    ent_id = Column(Text)
    ent_name = Column(Text)
    ent_addr1 = Column(Text)
    ent_city = Column(Text)
    ent_st_abbr = Column(Text)
    ent_zip = Column(Text)
    ent_phone = Column(Text)
    source_row_id = Column(Text)
    source_created_at = Column(DateTime(timezone=True))
    source_updated_at = Column(DateTime(timezone=True))
    batch_id = Column(Text)
    raw_json = Column(JSONB)
    inserted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

class IlEntityClient(Base):
    __tablename__ = 'il_entity_clients'

    il_entity_clients_pk = Column(Text, primary_key=True)
    ent_reg_year = Column(Integer)
    entity_id = Column(Text)
    entity_name = Column(Text)
    client_id = Column(Text)
    client_name = Column(Text)
    source_row_id = Column(Text)
    source_created_at = Column(DateTime(timezone=True))
    source_updated_at = Column(DateTime(timezone=True))
    batch_id = Column(Text)
    raw_json = Column(JSONB)
    inserted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

class IlExclusiveLobbyist(Base):
    __tablename__ = 'il_exclusive_lobbyists'

    il_exclusive_pk = Column(Text, primary_key=True)
    ent_reg_year = Column(Integer)
    ent_id = Column(Text)
    entity_name = Column(Text)
    lobbyist_id = Column(Text)
    lobbyist_name = Column(Text)
    source_row_id = Column(Text)
    source_created_at = Column(DateTime(timezone=True))
    source_updated_at = Column(DateTime(timezone=True))
    batch_id = Column(Text)
    raw_json = Column(JSONB)
    inserted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

class LobbyingAll(Base):
    __tablename__ = 'lobbying_all'

    source_state = Column(Text, primary_key=True)
    source_dataset = Column(Text, primary_key=True)
    source_unique_id = Column(Text, primary_key=True)
    reporting_year = Column(Integer)
    reporting_period = Column(Text)
    lobbyist_name = Column(Text)
    individual_lobbyist_name = Column(Text)
    client_name = Column(Text)
    beneficial_client_name = Column(Text)
    government_body = Column(Text)
    party_lobbied = Column(Text)
    subject = Column(Text)
    focus_type = Column(Text)
    amount = Column(Numeric(14, 2))
    load_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    raw_row = Column(JSONB)

class LobbyingEngagement(Base):
    __tablename__ = 'lobbying_engagements'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    jurisdiction = Column(Text, nullable=False)
    source_system = Column(Text, nullable=False)
    form_submission_id = Column(Text)
    unique_external_id = Column(Text, unique=True)
    reporting_year = Column(Text)
    filing_type = Column(Text)
    principal_lobbyist_name = Column(Text)
    principal_lobbyist_id = Column(Text)
    contractual_client_name = Column(Text)
    contractual_client_id = Column(Text)
    beneficial_client_name = Column(Text)
    beneficial_client_id = Column(Text)
    type_of_lobbying_relationship = Column(Text)
    level_of_government = Column(Text)
    description_of_agreement = Column(Text)
    reportable_compensation = Column(Text)
    compensation_amount = Column(Numeric)
    compensation_currency = Column(Text, server_default='USD')
    compensation_type = Column(Text)
    contract_start_date = Column(Date)
    contract_end_date = Column(Date)
    lobbying_subjects = Column(Text)
    lobbying_focus_type = Column(Text)
    focus_identifying_number = Column(Text)
    rbr_submitted = Column(Boolean)
    raw_source_url = Column(Text)
    raw_record = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_seen_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint('jurisdiction', 'source_system', 'unique_external_id', name='lobbying_engagements_jurisdiction_source_system_unique_exte_key'),
    )

class NyLobbyistBimonthly(Base):
    __tablename__ = 'ny_lobbyist_bimonthly'

    unique_id = Column(Text, primary_key=True)
    form_submission_id = Column(BigInteger)
    reporting_year = Column(Integer)
    filing_type = Column(Text)
    reporting_period = Column(Text)
    principal_lobbyist_name = Column(Text)
    contractual_client_name = Column(Text)
    beneficial_client_name = Column(Text)
    co_lobbyist = Column(Text)
    sub_lobbyist = Column(Text)
    individual_lobbyist_name = Column(Text)
    compensation = Column(Numeric(14, 2))
    reimbursed_expenses = Column(Numeric(14, 2))
    expenses_less_than_75 = Column(Numeric(14, 2))
    lobbying_expenses_for_non = Column(Numeric(14, 2))
    itemized_expenses = Column(Numeric(14, 2))
    expense_type = Column(Text)
    expense_paid_to = Column(Text)
    expense_reimbursed_by_client = Column(Text)
    expense_purpose = Column(Text)
    expense_date = Column(DateTime(timezone=True))
    expense_details_name = Column(Text)
    expense_details_title = Column(Text)
    expense_details_employer = Column(Text)
    expense_details_amount = Column(Numeric(14, 2))
    coalition_name = Column(Text)
    contribution_amount = Column(Numeric(14, 2))
    was_an_expense_incurred_on = Column(Text)
    total_amount_of_the_expense = Column(Numeric(14, 2))
    was_the_expense_paid_for = Column(Text)
    if_pooled_funds_were_used = Column(Numeric(14, 2))
    total_contribution_amount = Column(Numeric(14, 2))
    coalition_contribution_expense = Column(Text)
    lobbying_subjects = Column(Text)
    level_of_government = Column(Text)
    lobbying_focus_type = Column(Text)
    focus_identifying_number = Column(Text)
    type_of_lobbying_communication = Column(Text)
    government_body = Column(Text)
    monitoring_only = Column(Text)
    party_name = Column(Text)
    person_lobbied = Column(Text)
    department_lobbied = Column(Text)
    load_timestamp = Column(DateTime(timezone=True), server_default=func.now())

class ScPrincipal(Base):
    __tablename__ = 'sc_principals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    jurisdiction = Column(Text, nullable=False)
    principal_name = Column(Text, nullable=False)
    contact_first_name = Column(Text)
    contact_last_name = Column(Text)
    address = Column(Text)
    city = Column(Text)
    state_code = Column(Text)
    zipcode = Column(Text)
    phone = Column(Text)
    principal_key = Column(Text, nullable=False, index=True)
    enriched = Column(Boolean, nullable=False, server_default='false')
    last_enriched_at = Column(DateTime(timezone=True))

class Target(Base):
    __tablename__ = 'targets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    type = Column(Text)
    jurisdictions = Column(ARRAY(Text), server_default='{}')
    active = Column(Boolean, server_default='true')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        CheckConstraint("type IN ('individual', 'entity')", name='targets_type_check'),
    )

class WaLobbyistAgent(Base):
    __tablename__ = 'wa_lobbyist_agents'

    wa_lobbyist_agents_pk = Column(Text, primary_key=True)
    employment_year = Column(Integer)
    agent_id = Column(Text)
    agent_name = Column(Text)
    lobbyist_firm_name = Column(Text)
    lobbyist_phone = Column(Text)
    lobbyist_email = Column(Text)
    lobbyist_address = Column(Text)
    employers = Column(Text)
    lobbyist_firm_url = Column(Text)
    agent_pic_url = Column(Text)
    training_certified = Column(DateTime(timezone=True))
    batch_id = Column(Text)
    raw_json = Column(JSONB)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

class WaLobbyistEmploymentReg(Base):
    __tablename__ = 'wa_lobbyist_employment_reg'

    wa_lobbyist_employment_reg_pk = Column(Text, primary_key=True)
    id = Column(Text)
    report_number = Column(Text)
    lobbyist_id = Column(Text)
    lobbyist_name = Column(Text)
    employer_id = Column(Text)
    employer_name = Column(Text)
    employment_year = Column(Integer)
    employment_url = Column(Text)
    employment_period = Column(JSONB)
    contractor_id = Column(Text)
    contractor_name = Column(Text)
    batch_id = Column(Text)
    raw_json = Column(JSONB)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class WaLobbyistEmploymentRegistration(Base):
    __tablename__ = 'wa_lobbyist_employment_registrations'

    wa_employment_pk = Column(Text, primary_key=True)
    report_number = Column(Text)
    lobbyist_id = Column(Text)
    lobbyist_name = Column(Text)
    employer_id = Column(Text)
    employer_name = Column(Text)
    contractor_id = Column(Text)
    contractor_name = Column(Text)
    employment_year = Column(Integer)
    employment_url = Column(Text)
    employment_period = Column(Text)
    batch_id = Column(Text)
    raw_json = Column(JSONB)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

class WaLobbyistEmployment(Base):
    __tablename__ = 'wa_lobbyist_employments'

    wa_employment_pk = Column(Text, primary_key=True)
    report_number = Column(Text)
    lobbyist_id = Column(Text)
    lobbyist_name = Column(Text)
    employer_id = Column(Text)
    employer_name = Column(Text)
    employment_year = Column(Integer)
    contractor_id = Column(Text)
    contractor_name = Column(Text)
    employment_url = Column(Text)
    employment_period_raw = Column(Text)
    batch_id = Column(Text)
    raw_json = Column(JSONB, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)