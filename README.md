# Passkey Provider AAGUIDs

This is a **community-driven** list of known passkey provider AAGUIDs to assist with naming passkeys in end user passkey management interfaces (e.g. account settings). **It is not intended to be used for any other purpose** and **_could go away at any time_**. 

> [!IMPORTANT]  
> When this list is officially retired at some point in the future, the contents of both `aaguid.json` and `combined_aaguid.json` will be removed, **leaving an empty object**.
>
> It is **_highly_** recommended that you add some code that checks for an empty object after fetching the document (ex: `Object.keys(aaguid).length === 0`), and notifying the appropriate team(s). This README will also be updated with details.

This does not replace [FIDO's Metadata Service (MDS)](https://fidoalliance.org/metadata/), which should continue to be used for all authoritative security details about FIDO authenticators. Some AAGUIDs in this list may not appear in FIDO MDS.

A visual explorer of the list is available here: https://passkeydeveloper.github.io/passkey-authenticator-aaguids/explorer/

## Schema

For full details, see the latest JSON schema file: [https://github.com/passkeydeveloper/passkey-authenticator-aaguids/blob/main/aaguid.json.schema](https://github.com/passkeydeveloper/passkey-authenticator-aaguids/blob/main/aaguid.json.schema)

The top level property value is the AAGUID itself. For consistency in this file, ensure it is lowercase.

Each AAGUID member has at minimum, a `name` property. This property represents the friendly name of the passkey provider for display in RP interfaces. For example, "Google Password Manager", "Dashlane", or "1Password".

Each AAGUID member can also _optionally_ contain embedded icon data, for use next to the friendly name in RP interfaces.

The properties are `icon_dark` and `icon_light`. The values of these properties must be SVG data encoded into a base64 data URI. `icon_dark` should be a version targeted at dark mode and/or dark backgrounds. `icon_light` should be a version targeted at light mode and/or light backgrounds. The image must be square. The icon must be completely vector based and cannot contain embedded images (PNG, JPG, etc).

Many web-based tools can do this encoding/formatting, including: [https://base64.guru/converter/encode/image/svg](https://base64.guru/converter/encode/image/svg) (select `Data URI` under "Output Format").

Example of the Google G icon as a base64 encoded SVG data URI:

![]تحصیل پریس کلب رجسٹرڈ سرائے عالمگیر کی تق