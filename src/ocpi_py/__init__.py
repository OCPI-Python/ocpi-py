from enum import Enum
from typing import Annotated, Any, Callable, Dict, List, Optional, Sequence, Type, Union

from fastapi import APIRouter, FastAPI, Response, params
from fastapi.datastructures import Default
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from fastapi.types import IncEx
from fastapi.utils import generate_unique_id
from ocpi_pydantic.v221.versions import OcpiVersion, OcpiVersionDetail, OcpiVersionsResponse, OcpiVersionDetailsResponse, OcpiEndpoint
from starlette.routing import BaseRoute



class OcpiApp(FastAPI):
    def __init__(
            self, *, debug = False, routes = None, title = "FastAPI", summary = None, description = "", version = "0.1.0", openapi_url = "/openapi.json", openapi_tags = None, servers = None, dependencies = None, default_response_class = ..., redirect_slashes = True, docs_url = "/docs", redoc_url = "/redoc", swagger_ui_oauth2_redirect_url = "/docs/oauth2-redirect", swagger_ui_init_oauth = None, middleware = None, exception_handlers = None, on_startup = None, on_shutdown = None, lifespan = None, terms_of_service = None, contact = None, license_info = None, openapi_prefix = "", root_path = "", root_path_in_servers = True, responses = None, callbacks = None, webhooks = None, deprecated = None, include_in_schema = True, swagger_ui_parameters = None, generate_unique_id_function = ..., separate_input_output_schemas = True, openapi_external_docs = None, **extra
        ):
        super().__init__(
            debug=debug, routes=routes, title=title, summary=summary, description=description, version=version, openapi_url=openapi_url, openapi_tags=openapi_tags, servers=servers, dependencies=dependencies, default_response_class=default_response_class, redirect_slashes=redirect_slashes, docs_url=docs_url, redoc_url=redoc_url, swagger_ui_oauth2_redirect_url=swagger_ui_oauth2_redirect_url, swagger_ui_init_oauth=swagger_ui_init_oauth, middleware=middleware, exception_handlers=exception_handlers, on_startup=on_startup, on_shutdown=on_shutdown, lifespan=lifespan, terms_of_service=terms_of_service, contact=contact, license_info=license_info, openapi_prefix=openapi_prefix, root_path=root_path, root_path_in_servers=root_path_in_servers, responses=responses, callbacks=callbacks, webhooks=webhooks, deprecated=deprecated, include_in_schema=include_in_schema, swagger_ui_parameters=swagger_ui_parameters, generate_unique_id_function=generate_unique_id_function, separate_input_output_schemas=separate_input_output_schemas, openapi_external_docs=openapi_external_docs, **extra
        )



class OcpiAPIRouter(APIRouter):
    def __init__(
            self, *, prefix = "", tags = None, dependencies = None, default_response_class = ..., responses = None, callbacks = None, routes = None, redirect_slashes = True, default = None, dependency_overrides_provider = None, route_class = ..., on_startup = None, on_shutdown = None, lifespan = None, deprecated = None, include_in_schema = True, generate_unique_id_function = ...
        ):
        super().__init__(
            prefix=prefix, tags=tags, dependencies=dependencies, default_response_class=default_response_class, responses=responses, callbacks=callbacks, routes=routes, redirect_slashes=redirect_slashes, default=default, dependency_overrides_provider=dependency_overrides_provider, route_class=route_class, on_startup=on_startup, on_shutdown=on_shutdown, lifespan=lifespan, deprecated=deprecated, include_in_schema=include_in_schema, generate_unique_id_function=generate_unique_id_function
        )


    def get_versions(
        self,
        path: str = '/versions',
        *,
        response_model: Any = OcpiVersionsResponse,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[params.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Type[Response] = Default(JSONResponse),
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Callable[[APIRoute], str] = Default(generate_unique_id),
    ):
        return self.get(
            path=path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
        )
