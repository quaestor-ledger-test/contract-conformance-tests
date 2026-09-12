import "@typespec/json-schema";
using TypeSpec.JsonSchema;

namespace QuaestorLedgerObservation;

@id("ObservationPolicyV1")
model ObservationPolicyV1 {
  @minValue(1)
  @maxValue(1)
  version: integer;

  @minLength(1)
  @maxLength(128)
  ledger_id: string;

  @minValue(1)
  @maxValue(1000)
  batch_limit: integer;

  proof_required: boolean;

  @minValue(1)
  @maxValue(3650)
  retention_days: integer;
}
