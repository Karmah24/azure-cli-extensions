# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "self-help troubleshooter show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get troubleshooter instance result which includes the step status/result of the troubleshooter resource name that is being executed.

    :example: Show Troubleshooter at Resource Level
        az self-help troubleshooter show --troubleshooter-name 12345678-BBBb-cCCCC-0000-123456789123 --scope 'subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read'
    """

    _aaz_info = {
        "version": "2024-03-01-preview",
        "resources": [
            ["mgmt-plane", "/{scope}/providers/microsoft.help/troubleshooters/{}", "2024-03-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.scope = AAZStrArg(
            options=["--scope"],
            help="This is an extension resource provider and only resource level extension is supported at the moment.",
            required=True,
        )
        _args_schema.troubleshooter_name = AAZStrArg(
            options=["--troubleshooter-name"],
            help="Troubleshooter resource Name.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="([A-Za-z0-9]+(-[A-Za-z0-9]+)+)",
                max_length=100,
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.TroubleshootersGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class TroubleshootersGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/{scope}/providers/Microsoft.Help/troubleshooters/{troubleshooterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "scope", self.ctx.args.scope,
                    skip_quote=True,
                    required=True,
                ),
                **self.serialize_url_param(
                    "troubleshooterName", self.ctx.args.troubleshooter_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.parameters = AAZDictType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.solution_id = AAZStrType(
                serialized_name="solutionId",
            )
            properties.steps = AAZListType(
                flags={"read_only": True},
            )

            parameters = cls._schema_on_200.properties.parameters
            parameters.Element = AAZStrType()

            steps = cls._schema_on_200.properties.steps
            steps.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.steps.Element
            _element.automated_check_results = AAZObjectType(
                serialized_name="automatedCheckResults",
            )
            _element.description = AAZStrType()
            _element.error = AAZObjectType()
            _ShowHelper._build_schema_error_detail_read(_element.error)
            _element.execution_status = AAZStrType(
                serialized_name="executionStatus",
            )
            _element.execution_status_description = AAZStrType(
                serialized_name="executionStatusDescription",
            )
            _element.guidance = AAZStrType()
            _element.id = AAZStrType()
            _element.inputs = AAZListType()
            _element.insights = AAZListType()
            _element.is_last_step = AAZBoolType(
                serialized_name="isLastStep",
            )
            _element.title = AAZStrType()
            _element.type = AAZStrType()

            automated_check_results = cls._schema_on_200.properties.steps.Element.automated_check_results
            automated_check_results.result = AAZStrType()
            automated_check_results.type = AAZStrType()

            inputs = cls._schema_on_200.properties.steps.Element.inputs
            inputs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.steps.Element.inputs.Element
            _element.question_content = AAZStrType(
                serialized_name="questionContent",
            )
            _element.question_content_type = AAZStrType(
                serialized_name="questionContentType",
            )
            _element.question_id = AAZStrType(
                serialized_name="questionId",
            )
            _element.question_type = AAZStrType(
                serialized_name="questionType",
            )
            _element.recommended_option = AAZStrType(
                serialized_name="recommendedOption",
            )
            _element.response_hint = AAZStrType(
                serialized_name="responseHint",
            )
            _element.response_options = AAZListType(
                serialized_name="responseOptions",
            )
            _element.response_validation_properties = AAZObjectType(
                serialized_name="responseValidationProperties",
            )
            _element.selected_option_value = AAZStrType(
                serialized_name="selectedOptionValue",
            )

            response_options = cls._schema_on_200.properties.steps.Element.inputs.Element.response_options
            response_options.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.steps.Element.inputs.Element.response_options.Element
            _element.key = AAZStrType()
            _element.value = AAZStrType()

            response_validation_properties = cls._schema_on_200.properties.steps.Element.inputs.Element.response_validation_properties
            response_validation_properties.is_required = AAZBoolType(
                serialized_name="isRequired",
            )
            response_validation_properties.max_length = AAZIntType(
                serialized_name="maxLength",
            )
            response_validation_properties.regex = AAZStrType()
            response_validation_properties.validation_error_message = AAZStrType(
                serialized_name="validationErrorMessage",
            )

            insights = cls._schema_on_200.properties.steps.Element.insights
            insights.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.steps.Element.insights.Element
            _element.id = AAZStrType()
            _element.importance_level = AAZStrType(
                serialized_name="importanceLevel",
            )
            _element.results = AAZStrType()
            _element.title = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_error_detail_read = None

    @classmethod
    def _build_schema_error_detail_read(cls, _schema):
        if cls._schema_error_detail_read is not None:
            _schema.additional_info = cls._schema_error_detail_read.additional_info
            _schema.code = cls._schema_error_detail_read.code
            _schema.details = cls._schema_error_detail_read.details
            _schema.message = cls._schema_error_detail_read.message
            _schema.target = cls._schema_error_detail_read.target
            return

        cls._schema_error_detail_read = _schema_error_detail_read = AAZObjectType()

        error_detail_read = _schema_error_detail_read
        error_detail_read.additional_info = AAZListType(
            serialized_name="additionalInfo",
            flags={"read_only": True},
        )
        error_detail_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_detail_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.target = AAZStrType(
            flags={"read_only": True},
        )

        additional_info = _schema_error_detail_read.additional_info
        additional_info.Element = AAZObjectType()

        _element = _schema_error_detail_read.additional_info.Element
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_detail_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_detail_read(details.Element)

        _schema.additional_info = cls._schema_error_detail_read.additional_info
        _schema.code = cls._schema_error_detail_read.code
        _schema.details = cls._schema_error_detail_read.details
        _schema.message = cls._schema_error_detail_read.message
        _schema.target = cls._schema_error_detail_read.target


__all__ = ["Show"]
