import "@typespec/json-schema";
using TypeSpec.JsonSchema;

namespace QuaestorLedger;

@id("LedgerEntryV1")
model LedgerEntryV1 {
  @minValue(1)
  @maxValue(1)
  version: integer;

  @minLength(1)
  @maxLength(128)
  account_id: string;

  @minValue(0)
  @maxValue(1000000000000)
  debit_minor: integer;

  @minValue(0)
  @maxValue(1000000000000)
  credit_minor: integer;

  @minLength(3)
  @maxLength(3)
  currency: string;

  posted: boolean;
}
